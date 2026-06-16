---
layout: default
title: Efmoroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 259
evidence_level: L5
indication_count: 10
---

# Efmoroctocog Alfa
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

# Efmoroctocog Alfa：從血友病A到假性馮威里氏病

## 一句話總結

Efmoroctocog alfa 是一種重組第VIII凝血因子（rFVIII）與人類IgG1 Fc片段的融合蛋白，藉由FcRn介導的回收機制延長半衰期，原本用於血友病A（先天性FVIII缺乏症）的預防與治療。TxGNN 模型預測它可能對**假性馮威里氏病 (pseudo-von Willebrand disease)** 有效，惟目前**無任何臨床試驗或文獻**支持，證據僅止於模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 血友病A（先天性第VIII凝血因子缺乏症） |
| 預測新適應症 | 假性馮威里氏病 (pseudo-von Willebrand disease) |
| TxGNN 預測分數 | 99.997% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，efmoroctocog alfa（商品名 Elocta®）是將重組人類凝血第VIII因子與IgG1 Fc片段融合而成的長效蛋白質藥物。其核心機轉為：靜脈注射後，Fc片段與血管內皮細胞的新生兒Fc受體（FcRn）結合，被回收再循環至血流，使有效半衰期較傳統rFVIII延長約1.5倍。藥物進入凝血瀑布後，以輔因子角色加速FXa生成，恢復內源性凝血功能。

假性馮威里氏病（Pseudo-vWD，又稱血小板型vWD）是由血小板表面GPIbα糖蛋白發生**功能增益突變**所引起的稀有出血疾患。突變使血小板對馮威里氏因子（vWF）的親和力異常升高，導致多聚體型vWF被血小板過度結合並加速清除，形成血小板減少及出血傾向。

**機轉關聯性極低**：Pseudo-vWD 的根本病理在於 GPIbα 受體功能異常，繼而引發 vWF 消耗。雖然 vWF 在循環中會攜帶並穩定 FVIII，但補充 FVIII 無法修正 GPIbα 的結構缺陷，亦無法遏止 vWF 的過度清除。TxGNN 模型的預測可能源自知識圖譜中 vWF–FVIII 複合體的緊密生物學關聯，但臨床上兩者的治療邏輯截然不同。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Efmoroctocog alfa 目前在香港尚未取得上市許可，無藥品許可證資料可供查閱。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅有模型輸出（L5），**零臨床試驗、零文獻**支持，不符合進入評估流程的最低證據門檻。
- 機轉分析顯示，FVIII 補充與 Pseudo-vWD 的核心病理（GPIbα 功能增益突變導致 vWF 消耗）缺乏直接關聯，再利用合理性極低。

**若要推進需要：**
- 補齊 efmoroctocog alfa 的完整作用機轉（MOA）及安全性資料（建議查詢 DrugBank API）
- 評估 Pseudo-vWD 患者是否因繼發性 vWF 消耗導致 FVIII 水平下降，是否存在補充 FVIII 的理論窗口
- 搜尋 Pseudo-vWD 中 FVIII 替代治療的前臨床或個案研究（包含 FVIII–vWF 結合動力學研究）
- 優先審視其他評分更高且機轉更合理的候選適應症（如排名第9：血友病A合併血管異常，L3；排名第5：後天性凝血因子缺乏症，L4）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

