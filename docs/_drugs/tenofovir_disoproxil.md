---
layout: default
title: Tenofovir Disoproxil
parent: 僅模型預測 (L5)
nav_order: 844
evidence_level: L5
indication_count: 4
---

# Tenofovir Disoproxil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Tenofovir Disoproxil：從 HIV-1 感染到猴免疫缺陷病毒感染

## 一句話總結

Tenofovir Disoproxil (TDF) 是 tenofovir 的前驅藥，屬核苷酸反轉錄酶抑制劑，已核准用於人類 HIV-1 感染。
TxGNN 模型預測它可能對**猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection)** 有效。
不過目前只有 **2 個間接相關的臨床試驗**（一個撤回、一個狀態不明），**沒有文獻**支持。SIV 本身就是 HIV 的非人靈長類動物模型，所以這不算新的人類適應症訊號。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L5（僅有模型預測，無直接研究；資料包初步標示為 L4，但提供的試驗均非 SIV 研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 TDF 是 tenofovir 的前驅藥，屬核苷酸反轉錄酶抑制劑，並已核准用於人類 HIV-1 感染。

SIV 與 HIV 同屬慢病毒，共享反轉錄酶的生物學特性，所以知識圖譜把兩者連起來在機轉上說得通。但 SIV 是 HIV-1 的動物模型，這個預測其實是在重述已知適應症，不是發現新的人類用途。

此外，該預測的其他候選疾病訊號更弱：
- **貓後天免疫缺乏症候群 (FIV)**：有 2 篇動物研究（含直接測試 PMPA/tenofovir 的貓研究），但價值僅限於獸醫或前臨床。
- **伴隨共濟失調步態、無語言與皮質白質減少的神經發育障礙**：無可信的機轉連結，無任何試驗或文獻。
- **家族性複合型高脂血症（已過時術語）**：無明確機轉連結，可能是本體論對應造成的假訊號。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | N/A | 已撤回 | 0 | 以 raltegravir 研究 HIV 病毒衰減動力學。並非 SIV 研究，TDF 也不是受試介入，且未產生任何資料 |
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | 狀態不明 | 12 | Vedolizumab 合併抗反轉錄病毒療法，用於未曾治療的 HIV 感染者以追求持久病毒學緩解。TDF 至多是背景療法，屬間接證據，且疾病為人類 HIV 而非 SIV |

---

## 文獻證據

目前無相關文獻

---

## 香港上市資訊

香港共有 20 張含 TDF 的許可證，以下列出 5 張主要許可證（資料中未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-65666 | TENO B TABLETS 300MG | JACOBSON MARKETING LIMITED |
| HK-67751 | FORVIC 300 TABLETS 300MG | HEALTH ALLIANCE INTERNATIONAL CO LTD |
| HK-64889 | TENOFOVIR DISOPROXIL FUMARATE TABLETS 300MG | SINO PACIFIC PHARMA COMPANY LIMITED |
| HK-56075 | VIREAD TAB 300MG | GILEAD SCIENCES HONG KONG LIMITED |
| HK-65885 | TENOFOVIR SANDOZ TABLETS 300MG | SANDOZ HONG KONG LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 唯一與 SIV 直接相關的試驗已撤回、未收案；另一個試驗狀態不明，TDF 只是背景療法。
- 沒有任何文獻。
- SIV 是 HIV-1 的動物模型，而 TDF 已核准用於人類 HIV-1，所以這個預測沒有新的人類臨床價值。

**若要推進需要：**
- 確認是否有 TDF 或 tenofovir 直接用於 SIV 的前臨床研究（目前提供的資料中沒有）。
- 補齊原適應症與核准適應症文字。香港衛生署許可證目前沒有適應症內容。
- 取得香港衛生署仿單的警語與禁忌症，才能進行安全性篩選。
- 補齊 DrugBank 的作用機轉資料。
- 若目標是新的人類適應症，應轉向其他候選疾病，或重新篩選預測結果。

---

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

