---
layout: default
title: Pioglitazone
parent: 僅模型預測 (L5)
nav_order: 686
evidence_level: L5
indication_count: 5
---

# Pioglitazone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Pioglitazone：從第二型糖尿病到 Opsismodysplasia

## 一句話總結

Pioglitazone 是一種 PPARγ 促效劑（胰島素增敏劑），一般用於第二型糖尿病，但本次提供的香港許可證資料未載明適應症文字。
TxGNN 模型預測它可能對**Opsismodysplasia（一種罕見骨骼發育不良）**有效。
目前**沒有臨床試驗，也沒有文獻**支持，僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明（Pioglitazone 一般用於第二型糖尿病） |
| 預測新適應症 | Opsismodysplasia |
| TxGNN 預測分數 | 99.59% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 機轉欄位為空）。Pioglitazone 是 PPARγ 促效劑，能提高胰島素敏感性。以下機轉連結僅為推測，沒有任何證據支持。

Opsismodysplasia 與 *INPPL1*（SHIP2）基因變異有關。SHIP2 參與 PI3K／胰島素訊息傳遞，因此與 pioglitazone 的胰島素增敏作用在訊息路徑上可能有交集。但是否能讓骨骼發育不良的病人獲益，目前沒有任何資料。

預測分數雖高（99.59%），但這是模型從知識圖譜推論的結果，不是臨床證據。須先以文獻與前臨床研究驗證，才能判斷是否值得推進。

### 其他預測適應症（同為 L5、Hold）

| 排名 | 預測適應症 | TxGNN 分數 | 推測的機轉連結 |
|------|-----------|-----------|---------------|
| 2 | Focal stiff limb syndrome | 99.50% | PPARγ 促效劑的抗發炎與免疫調節作用，尚未驗證 |
| 3 | Classic stiff person syndrome | 99.50% | 抗 GAD 自體免疫疾病常合併糖尿病，可能有免疫調節效果，無臨床支持 |
| 4 | Thiamine-responsive dysfunction syndrome | 99.48% | 可能只反映糖尿病的關聯，pioglitazone 不處理硫胺素轉運問題，合理性低 |
| 5 | Drug-induced localized lipodystrophy | 99.30% | PPARγ 促進脂肪細胞分化，噻唑烷二酮類曾用於其他脂肪失養症，是五個中生物學上最合理者，但仍是假說 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張主要許可證。許可證資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-57967 | ZOLID TAB 45MG | CHARIOT PHARMA LIMITED |
| HK-47884 | ACTOS TAB 30MG | SYNMOSA BIOPHARMA (HONG KONG) COMPANY LIMITED |
| HK-47882 | ACTOS TAB 15MG | SYNMOSA BIOPHARMA (HONG KONG) COMPANY LIMITED |
| HK-58692 | APO-PIOGLITAZONE TAB 30MG | HIND WING CO LTD |
| HK-56745 | GLITTER-15 TAB 15MG | UNIPHARM (HONG KONG) LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 只有模型預測（L5），沒有臨床試驗或文獻，且 pioglitazone 與骨骼發育不良之間沒有已知的治療關聯。
- 香港衛生署仿單的警語與禁忌資料也尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單（警語與禁忌症），補齊安全性資料
- 從 DrugBank 補齊 pioglitazone 的作用機轉
- 針對 Opsismodysplasia 與 INPPL1／SHIP2 通路進行文獻檢索，驗證推測的機轉連結
- 優先檢索藥物引發的局部脂肪失養症（排名 5），其生物學合理性最高，可作為第一個驗證目標

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

