---
layout: default
title: Cefuroxime
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
---

# Cefuroxime
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Cefuroxime：從（原適應症資料缺漏）到高澱粉酶血症

## 一句話總結

Cefuroxime 是第二代頭孢菌素類抗生素，Evidence Pack 未提供原適應症資料。
TxGNN 模型預測它可能對**高澱粉酶血症 (Hyperamylasemia)** 有效，但目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測訊號。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 高澱粉酶血症 (Hyperamylasemia) |
| TxGNN 預測分數 | 99.76% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 為資料缺口）。Cefuroxime 是頭孢菌素類抗生素，一般用於細菌感染，但本次資料未列出原適應症，無法比對新舊適應症的關聯。

高澱粉酶血症是血中澱粉酶升高的檢驗異常，常見於胰臟或唾液腺疾病。目前找不到抗生素直接作用於此狀態的機轉依據，也沒有任何研究可佐證。

這個預測分數很高（99.76%），但僅反映知識圖譜的統計關聯，不能視為療效證據。在取得機轉或臨床資料前，應把它當作待驗證的假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-61702 | AXCEF TABLETS 250MG | LSB (HK) LIMITED |
| HK-55257 | SEFUXIM TAB 250MG | CEUTICAL TRADING COMPANY LIMITED |
| HK-52841 | CEFUROXIME SODIUM FOR INJ 750MG | JINDUN PHARMA (H.K.) LIMITED |
| HK-29697 | ZINNAT TAB 500MG | SANDOZ HONG KONG LIMITED |
| HK-63784 | AXCEL CEFUROXIME-250 CAPSULES 250MG | KOTRA PHARMA (HONG KONG) COMPANY |

（共 20 張許可證，此處列出 5 張；資料中劑型與核准適應症皆為空白。）

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這是純模型預測，沒有試驗、文獻或機轉支持，證據等級為 L5。
- 香港仿單的警語與禁忌資料尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 從香港衛生署取得仿單，確認核准適應症與安全性資訊。
- 從 DrugBank 補齊作用機轉資料。
- 針對高澱粉酶血症做文獻檢索，找出可能的生物學連結。
- 另外，同一藥物排名較後的預測中，「尿路感染」有較多證據（L3、建議 Proceed with Guardrails）。若要優先評估，建議改以該適應症為主軸，並先確認它是否為已核准的標示適應症。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

