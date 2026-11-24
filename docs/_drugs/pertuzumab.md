---
layout: default
title: Pertuzumab
parent: 僅模型預測 (L5)
nav_order: 685
evidence_level: L5
indication_count: 6
monitor_inn: "PERTUZUMAB"
predicted_indications: ["ectomesenchymoma", "malignant cutaneous granular cell skin tumor", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma"]
last_modified_at: 2026-11-24
description: "Pertuzumab：預測新適應症為外胚間葉瘤 (Ectomesenchymoma)（證據等級 L5）。原適應症：HER2 陽性乳癌"
---

# Pertuzumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Pertuzumab：從 HER2 陽性乳癌到外胚間葉瘤（Ectomesenchymoma）
{: .text-alpha }

## 一句話總結

Pertuzumab 是一種標靶 HER2 的單株抗體，知識圖譜中記錄的原適應症為 HER2 陽性乳癌。
TxGNN 模型預測它可能對**外胚間葉瘤 (Ectomesenchymoma)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬於模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HER2 陽性乳癌（來自知識圖譜的記錄關係；本地許可證資料未提供適應症文字） |
| 預測新適應症 | 外胚間葉瘤 (Ectomesenchymoma) |
| TxGNN 預測分數 | 0.9971 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Pertuzumab 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Pertuzumab 以人類表皮生長因子受體 2 蛋白（HER2）的細胞外二聚化結構域（Subdomain II）為標靶，從而阻斷 HER2 與其他 HER 家族成員（包括 EGFR、HER3 及 HER4）之間依賴配體的異二聚化。因此，pertuzumab 可抑制由配體啟動、經由兩條主要訊息路徑——絲裂原活化蛋白（MAP）激酶及磷酸肌醇 3-激酶（PI3K）——進行的細胞內訊息傳遞。」英文原文："Pertuzumab targets the extracellular dimerization domain (Subdomain II) of the human epidermal growth factor receptor 2 protein (HER2) and, thereby, blocks ligand-dependent heterodimerization of HER2 with other HER family members, including EGFR, HER3, and HER4. As a result, pertuzumab inhibits ligand-initiated intracellular signaling through two major signal pathways, mitogen-activated protein (MAP) kinase, and phosphoinositide 3-kinase (PI3K)."（[DailyMed: Perjeta (pertuzumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=17f85d17-ab71-4f5b-9fe3-0b8c822f69ff)，版本日期 2026-04-30；查閱日期 2026-11-19）。根據已知資訊，Pertuzumab 是針對 HER2 受體的單株抗體，藥理資料庫顯示其標的為 ERBB2，臨床用途為 HER2 過度表現的乳癌。一般認為它會阻斷 HER2 與 HER3 等 HER 家族受體的二聚化。

外胚間葉瘤是一種極罕見、含神經外胚層與間葉成分的混合型腫瘤。目前提供的資料中，並沒有顯示此腫瘤依賴 HER2 訊號。因此這個預測的機轉連結屬於推測，分數雖高，但僅為計算預測。

若要進一步論證，首先需要確認此腫瘤是否有 HER2 表現或擴增。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-62758 | PERJETA CONCENTRATE FOR SOLUTION FOR INFUSION 420MG | 單一成分 | ROCHE HONG KONG LIMITED | 有效 |
| HK-67118 | PHESGO SOLUTION FOR SUBCUTANEOUS INJECTION 1200MG/600MG IN 15ML | 複方 | ROCHE HONG KONG LIMITED | 有效 |
| HK-67119 | PHESGO SOLUTION FOR SUBCUTANEOUS INJECTION 600MG/600MG IN 10ML | 複方 | ROCHE HONG KONG LIMITED | 有效 |

<!-- licenses:end -->

以上三張許可證均為有效，持證商為 ROCHE HONG KONG LIMITED。

## 細胞毒性

Pertuzumab 屬標靶抗體藥物（非傳統細胞毒性化療藥物），用於抗腫瘤治療。本次資料未提供骨髓抑制、致吐性等細胞毒性資料，請參考原廠仿單的警語與注意事項。

## 安全性考量

- **藥物交互作用**：資料庫記錄與 Idelalisib 有中度（Moderate）等級的交互作用。

其餘警語與禁忌症資料，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自模型計算，沒有任何針對外胚間葉瘤的臨床試驗或文獻，證據等級為 L5。
- 此腫瘤是否依賴 HER2 訊號並無資料支持，機轉連結屬推測。

**若要推進需要：**
- 檢測外胚間葉瘤組織的 HER2 表現或擴增狀態
- 系統性搜尋 HER2 標靶治療於此類罕見腫瘤的文獻與病例報告
- 補充 Pertuzumab 的作用機轉資料
- 取得香港仿單的警語與禁忌症，以進行安全性評估

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Perjeta (pertuzumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=17f85d17-ab71-4f5b-9fe3-0b8c822f69ff) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

