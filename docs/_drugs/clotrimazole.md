---
layout: default
title: Clotrimazole
parent: 僅模型預測 (L5)
nav_order: 221
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "CLOTRIMAZOLE"
predicted_indications: ["acne (disease)", "postmenopausal atrophic vaginitis"]
description: "Clotrimazole：預測新適應症為痤瘡 (acne (disease))（證據等級 L5）。香港藥劑製品註冊：397 張（有效 396 張）"
---

# Clotrimazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

## Clotrimazole: 痤瘡 (acne (disease))
{: .text-alpha }

## 一句話總結

Clotrimazole 是一種外用與陰道用的唑類抗黴菌藥，在香港已有多張有效許可證。
TxGNN 模型預測它可能對**痤瘡 (acne (disease))** 有效，分數為 0.9986。
目前僅有 **1 個臨床試驗**（為三合一複方、已暫停），且**無文獻**直接支持，證據仍相當薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 痤瘡 (acne (disease)) |
| TxGNN 預測分數 | 0.9986 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 396 張／共 397 張） |
| 許可證數 | 397 張（有效 396 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Clotrimazole 處方資料（Prescribing Information）「Clinical Pharmacology」段（非官方翻譯）：「Clotrimazole 是一種廣效抗真菌藥物，可經由改變細胞膜的通透性而抑制致病性酵母菌的生長。Clotrimazole 在藥物濃度達 20 mcg/mL 以下時具抑制真菌作用，而在較高濃度時，於體外可能對白色念珠菌（Candida albicans）及念珠菌屬（Candida）其他菌種具殺真菌作用。」英文原文："Clotrimazole is a broad-spectrum antifungal agent that inhibits the growth of pathogenic yeasts by altering the permeability of cell membranes. The action of clotrimazole is fungistatic at concentrations of drug up to 20 mcg/mL and may be fungicidal in vitro against Candida albicans and other species of the genus Candida at higher concentrations."（[DailyMed: clotrimazole prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=980736aa-751a-4642-ab85-a309435fd02f)，版本日期 2025-03-27；查閱日期 2026-11-19）。就已知資訊，Clotrimazole 屬於唑類抗黴菌藥，一般認為其作用是抑制黴菌 CYP51 酵素，阻斷麥角固醇合成。另有報告指出它具有一定的抗菌與抗發炎活性。

在機轉上，可能的連結是痤瘡毛囊發炎與 Malassezia 或 Cutibacterium 有關，但這一點屬推測。唯一找到的試驗使用的是 beclomethasone、gentamicin 與 clotrimazole 的固定複方，無法分辨療效是否來自 clotrimazole。

0.9986 是模型的計算結果，不能取代臨床證據。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | 暫停 | 80 | 比較 beclomethasone + gentamicin + clotrimazole 複方乳膏，用於雙側對稱性皮損的污染性皮膚炎；無完成結果，且無法分離 clotrimazole 的貢獻 |

此試驗為複方製劑，所研究的病症是否確為痤瘡並不明確，只能視為間接證據。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-25433 | CANESTEN CREAM 1% | 單一成分 | BAYER HEALTHCARE LIMITED | 有效 |
| HK-25432 | CANESTEN VAGINAL TAB 0.1G | 單一成分 | BAYER HEALTHCARE LIMITED | 有效 |
| HK-65884 | CANESTEN ANTI FUNGAL CREAM 1% W/W | 單一成分 | BAYER HEALTHCARE LIMITED | 有效 |
| HK-47412 | GEOVITE SKIN SPRAY 1% | 單一成分 | MEYER PHARMACEUTICALS LTD | 有效 |
| HK-65810 | CLOTRI CUTANEOUS SPRAY, SOLUTION 10MG/ML | 單一成分 | HITPHARM PHARMACEUTICAL CO LTD | 有效 |

上表列出其中 5 張（共 397 張）。

<!-- licenses:end -->

香港共有 397 張含本藥成分的許可證（有效 396 張、已註銷 1 張；單一成分 79 張、複方 318 張），此處僅列出其中 5 張。

<!-- review:begin hk-lic-20261117-clotrimazole-1 -->

> **查核更正（2026-11-17）**：原文為「本報告所整理的資料顯示共 20 張有效許可證，皆為單一成分製劑，此處僅列出其中 5 張，清單可能不完整。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 397 張含本藥成分的許可證（有效 396 張、已註銷 1 張；單一成分 79 張、複方 318 張）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-clotrimazole-1 -->

## 安全性考量

- **藥物交互作用**：共查得 100 筆交互作用紀錄。較重要的 Major 等級包括 Fentanyl、Alfentanil、Amiodarone、Hydrocodone；Moderate 等級包括 Paclitaxel、Abemaciclib、Acalabrutinib、Nifedipine、Amlodipine、Apixaban、Alprazolam 等。併用時應留意代謝酵素抑制所致的血中濃度上升。

其他警語與禁忌資料請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何研究直接針對 clotrimazole 單一成分用於痤瘡，唯一的試驗是已暫停的複方試驗，故證據等級為 L5。
- 機轉連結屬推測，高分僅反映模型計算結果。

**若要推進需要：**
- 取得詳細的作用機轉資料，並評估與痤瘡致病因子（如 Malassezia、Cutibacterium）的關聯
- 進行 clotrimazole 單一成分用於痤瘡的前臨床或小規模臨床研究
- 取得香港原廠仿單，補齊警語與禁忌資訊

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「本報告所整理的資料顯示共 20 張有效許可證，皆為單一成分製劑，此處僅列出其中 」→「香港共有 397 張含本藥成分的許可證（有效 396 張、已」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: clotrimazole prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=980736aa-751a-4642-ab85-a309435fd02f) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

