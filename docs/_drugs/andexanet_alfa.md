---
layout: default
title: Andexanet Alfa
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 4
---

# Andexanet Alfa
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

# Andexanet Alfa：從 FXa 抑制劑逆轉到 Glanzmann 血小板無力症

## 一句話總結

Andexanet alfa 是一種重組修飾 Factor Xa 蛋白，設計用於逆轉 Factor Xa 抑制劑（如 apixaban、rivaroxaban）的抗凝效應；台灣目前尚未取得上市許可。
TxGNN 模型預測它可能對 **Glanzmann 血小板無力症 (Glanzmann thrombasthenia)** 有效，
然而目前有 **0 個臨床試驗**和 **0 篇文獻**直接支持此方向，且機轉關聯性存在根本性疑慮。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | FXa 抑制劑相關出血逆轉（台灣未核准，無上市資料） |
| 預測新適應症 | Glanzmann 血小板無力症 (Glanzmann thrombasthenia) |
| TxGNN 預測分數 | 99.77% |
| 證據等級 | L5 |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

**作用機轉**

Evidence Pack 中缺乏正式的 MOA 記錄。根據公開資料，andexanet alfa 是一種重組修飾人類 Factor Xa（FXa）蛋白，其催化位點已去活化，設計作為 FXa 抑制劑的「誘餌受體（decoy receptor）」。透過競爭性結合 apixaban 或 rivaroxaban，andexanet alfa 能釋放內源性 FXa、恢復凝血酶原酶（prothrombinase）複合體活性，進而逆轉抗凝效應。

**原適應症與新適應症的關聯性**

Glanzmann 血小板無力症的病因為血小板表面整合素 GPIIb/IIIa（αIIbβ3）基因突變，導致血小板無法聚集纖維蛋白原，屬於**初級止血**路徑的障礙，臨床表現為黏膜出血和手術後出血不止。Andexanet alfa 的作用節點位於凝血瀑布的**二級止血**層級（FXa → 凝血酶原 → 凝血酶），兩者分屬截然不同的止血機制，在藥理上缺乏直接交集。

**預測可信度評估**

Evidence Pack 的機轉分析指出：TxGNN 的高預測分數（99.77%）很可能源於知識圖譜中「出血性疾病（hemostatic disorder）」大節點所帶來的**間接拓撲連結**，而非真實藥理機轉的支持。這是圖神經網路模型的已知局限——當兩種疾病在疾病本體（ontology）中共享廣義上位節點時，模型容易給出假陽性高分。**目前無任何臨床或機轉直接證據支持此預測。**

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
本預測屬 L5 等級（僅模型預測，無任何直接研究）。機轉分析明確顯示 andexanet alfa 的 FXa 逆轉機轉與 Glanzmann 血小板無力症的 GPIIb/IIIa 缺損路徑無直接交集，生物學可行性低；此預測高分判斷為知識圖譜拓撲結構造成的假陽性，不建議優先投入資源。

**若要推進需要：**
- 補充 andexanet alfa 完整 MOA 資料（建議查詢 DrugBank API，解決 DG002 資料缺口）
- 下載並解析 TFDA 原廠仿單 PDF，補足警語與禁忌資料（解決 DG001 Blocking 缺口）
- 搜尋 andexanet alfa 對血小板聚集功能是否存在任何旁觀效應（off-target effect）的基礎研究
- 重新檢視 TxGNN 知識圖譜的連結路徑，確認高分是否確實僅來自「出血性疾病」間接節點
- 台灣本地使用需先完成監管審查程序（進口藥品許可申請）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

