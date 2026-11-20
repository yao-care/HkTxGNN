---
layout: default
title: Nilotinib
parent: 僅模型預測 (L5)
nav_order: 619
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
monitor_inn: "NILOTINIB"
predicted_indications: ["dermatofibrosarcoma protuberans"]
description: "Nilotinib：預測新適應症為隆突性皮膚纖維肉瘤 (dermatofibrosarcoma protuberans)（證據等級 L5）。香港藥劑製品註冊：6 張（有效 6 張）"
---

# Nilotinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Nilotinib: 隆突性皮膚纖維肉瘤 (dermatofibrosarcoma protuberans)
{: .text-alpha }

## 一句話總結

Nilotinib 是一種酪胺酸激酶抑制劑，原本用於 BCR-ABL1 陽性的慢性骨髓性白血病。
TxGNN 模型預測它可能對**隆突性皮膚纖維肉瘤 (Dermatofibrosarcoma protuberans, DFSP)** 有效，
目前僅有 **1 篇文獻**（綜述類型），**尚無臨床試驗登記**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 隆突性皮膚纖維肉瘤 (dermatofibrosarcoma protuberans) |
| TxGNN 預測分數 | 0.9931 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 6 張／共 6 張） |
| 許可證數 | 6 張（有效 6 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Nilotinib 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Nilotinib為BCR-ABL激酶抑制劑。Nilotinib與ABL蛋白激酶結構域的非活化構形結合並使其穩定。在體外試驗中，nilotinib抑制了BCR-ABL介導的小鼠白血病細胞株及源自Ph+ CML病人之人類細胞株的增殖。」英文原文："Nilotinib is an inhibitor of the BCR-ABL kinase. Nilotinib binds to and stabilizes the inactive conformation of the kinase domain of ABL protein. In vitro, nilotinib inhibited BCR-ABL mediated proliferation of murine leukemic cell lines and human cell lines derived from patients with Ph+ CML."（[DailyMed: Cavhanza (nilotinib) prescribing information, Cycle Pharmaceuticals Ltd](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98b197ea-bca4-427e-8737-97f70a3262bc)，版本日期 2026-07-20；查閱日期 2026-11-19）。以下機轉推論來自 nilotinib 的一般藥理知識，仍需對照 DrugBank 或原廠資料確認。

Nilotinib 除了抑制 BCR-ABL1 之外，也會抑制 PDGFR-α/β 與 KIT。隆突性皮膚纖維肉瘤主要由 COL1A1-PDGFB 融合基因驅動，此融合會持續產生 PDGFB，造成 PDGFR-β 的自分泌活化。因此從標靶層面來看，用 nilotinib 阻斷 PDGFR 訊號有合理的生物學基礎。

目前唯一的文獻 (PMID 29408302, 2018) 是討論小分子 PDGFR 抑制劑在腫瘤治療角色的綜述。它支持「抑制 PDGFR 可用於此類腫瘤」的機轉方向，但**並非 nilotinib 專屬的臨床證據**。TxGNN 分數雖高，但屬於計算預測，不能視為臨床證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | 綜述小分子 PDGFR 抑制劑在腫瘤性疾病的治療角色；支持機轉方向，但非 nilotinib 專屬臨床證據 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-56797 | TASIGNA CAP 200MG | — | — |
| HK-60833 | TASIGNA CAP 150MG | — | — |

兩張許可證均為單一成分製劑，持有者為 Novartis Pharmaceuticals (HK) Limited，狀態皆為有效。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（酪胺酸激酶抑制劑） |
| 監測項目 | CBC（含分類）、肝功能、血糖、電解質（鉀、鈣、磷）、心電圖（QT 間期） |

其餘項目（致吐性分級、處置防護）請參考原廠仿單的警語與注意事項。

---

## 安全性考量

- **知識圖譜標示的禁忌/需謹慎疾病**（非仿單內容，僅供參考）：
  - 心血管：高血壓、long QT 症候群（含家族性）、torsades de pointes
  - 肝膽胰：肝病、膽囊疾病、高膽紅素血症（含 Gilbert 症候群）、胰臟炎
  - 血液：血小板低下、嗜中性白血球低下、顆粒球缺乏症、貧血（含巨球性貧血）
  - 代謝：高血糖、糖尿病、糖尿病酮酸中毒、低鉀、高鈣血症、腎鈣質沉著症、磷代謝異常、低磷血症

- **藥物交互作用**（共查得 100 筆，以下為部分重點）：
  - **重度 (Major)**：Dexamethasone、Clarithromycin、Picosulfuric acid、Polyethylene glycol（含電解質）
  - **中度 (Moderate)**：Famotidine、Ranitidine、Cimetidine、Omeprazole、Rabeprazole（制酸劑/PPI 類）；Hydrocortisone、Triamcinolone、Betamethasone、Budesonide（類固醇類）；Pioglitazone、Saxagliptin、Loperamide、Bupropion、Aprepitant、Bisacodyl

仿單的警語與禁忌資料尚未取得，完整安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 雖然 TxGNN 分數很高（0.9931），且 PDGFR 抑制的機轉推論合理，但目前只有一篇非 nilotinib 專屬的綜述，沒有臨床試驗，證據僅達 L4。
- 仿單的警語與禁忌資料尚未取得，無法進行安全性篩選。

**若要推進需要：**
- 補充 nilotinib 在 DFSP 的直接臨床證據（臨床試驗、病例報告或回溯性研究）
- 從 DrugBank 取得正式的作用機轉資料，驗證 PDGFR 抑制的機轉推論
- 取得香港衛生署的仿單，補齊警語與禁忌症，並評估 QT 延長、肝毒性與藥物交互作用風險
- 確認香港許可證核准適應症與劑型資訊（目前為空白）
- 與現有 DFSP 標準治療（如其他 PDGFR 抑制劑）比較，評估 nilotinib 的相對價值

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Cavhanza (nilotinib) prescribing information, Cycle Pharmaceuticals Ltd](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98b197ea-bca4-427e-8737-97f70a3262bc) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

