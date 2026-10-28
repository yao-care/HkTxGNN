---
layout: default
title: Haloperidol
parent: 僅模型預測 (L5)
nav_order: 433
evidence_level: L5
indication_count: 10
monitor_inn: "HALOPERIDOL"
predicted_indications: ["congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited", "syndromic myopia", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "atypical glycine encephalopathy", "manic bipolar affective disorder"]
last_modified_at: 2026-10-28
description: "Haloperidol：預測新適應症為Congenital disorder of glycosylation with defective fucosylation（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Haloperidol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Haloperidol: Congenital disorder of glycosylation with defective fucosylation
{: .text-alpha }

## 一句話總結

Haloperidol（鹵派啶醇）是一種抗精神病藥，知識圖譜記錄它與精神病性疾患、思覺失調症、妥瑞氏症等相關。
TxGNN 模型預測它可能對**岩藻糖基化缺陷型先天性糖基化異常**有效，但目前**沒有任何臨床試驗或文獻**直接支持，屬於純模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Congenital disorder of glycosylation with defective fucosylation |
| TxGNN 預測分數 | 0.9991 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 18 張／共 18 張） |
| 許可證數 | 18 張（有效 18 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Haloperidol 是多巴胺 D2 受體拮抗劑，用於精神科領域。

這個預測的高分來自模型運算。目前沒有找到 D2 拮抗作用與蛋白質糖基化、岩藻糖基化缺陷之間合理的機轉連結。這是先天性代謝性疾病，與抗精神病藥的作用標的相距甚遠。因此，我們把這個預測視為尚待驗證的假說，不能視為有實質依據的再利用方向。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

目前共有 18 張有效許可證，皆為單一成分，包含口服錠劑、口服滴劑、一般注射液與長效癸酸酯注射液。以下列出 5 張，許可證資料未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-64839 | HALOPERIDOL-NEURAXPHARM TABLETS 1MG | HIND WING CO LTD |
| HK-54962 | HALOPERIDOL INJ 5MG/ML | AMDIPHARM MERCURY (HONG KONG) LIMITED |
| HK-65060 | HALOPERIDOL-NEURAXPHARM DECANOATE SOLUTION FOR INJECTION 100MG/ML | HIND WING CO LTD |
| HK-65430 | HALOPERIDOL-NEURAXPHARM TABLETS 5MG | HIND WING CO LTD |
| HK-62669 | HALOPERIDOL KERN PHARMA ORAL DROPS 2MG/ML | HIND WING CO LTD |

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單文字）：
  - 心臟：長 QT 症候群、尖端扭轉型心室頻脈。
  - 神經：癲癇、基底核疾病、局部手部肌張力不全、眼瞼痙攣、惡性抗精神病藥症候群。
  - 血液：嗜中性白血球低下、顆粒球缺乏症、白血球低下。
  - 其他：肝病、膽囊疾病、甲狀腺功能低下、缺鉀、低血壓、女性乳癌。
- **藥物交互作用**：共記錄 100 筆，其中列為「嚴重」的包括 Bupropion、Morphine、Clarithromycin、Dolasetron；另有多項「中度」交互作用，如 Famotidine、Epinephrine、Hydrocortisone、Amphotericin B、Atropine 等。

香港仿單的警語與禁忌尚未取得，詳細安全性資訊請參考原廠仿單。

## 其他預測適應症的簡要說明

本次資料另有 9 個預測適應症，其中只有兩項有實質資料：

| 預測適應症 | 證據摘要 | 判斷 |
|-----------|---------|------|
| 躁症型雙相情緒障礙 | 有 Phase 3 試驗 NCT00129220（完成，224 人，安慰劑與 haloperidol 對照），另有多篇網絡統合分析。其餘兩項試驗與 haloperidol 的關聯未獲確認 | 與原本精神科用途接近，不算全新適應症。依本報告規則評為 L2 較為保守 |
| 視網膜失養症 | 僅有 2 篇大鼠視網膜神經節細胞電生理研究，屬描述藥理作用的前臨床研究，並非治療效果；方向可能有害 | 並非直接研究該疾病的療效，依規則為 L5 |

其餘預測適應症（水腦無腦症、X 連鎖近視、腓骨肌萎縮症 1G 型、症候群性近視、多小腦回畸形、非典型甘胺酸腦病變等）皆無研究支持，屬 L5。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有臨床試驗與文獻，也找不到合理的機轉連結，且 Haloperidol 的心臟與神經安全性疑慮不小。
- 現階段不建議投入資源推進。

**若要推進需要：**
- 補充 Haloperidol 的作用機轉資料，並探討糖基化／岩藻糖基化途徑是否有任何關聯。
- 先進行細胞或動物模型的機轉驗證。
- 取得香港仿單的警語與禁忌資料，完成安全性篩選。
- 若想評估精神科以外的方向，可優先檢視躁症的證據，因為它與原用途最接近。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

