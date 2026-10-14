---
layout: default
title: Methoxy Polyethylene Glycol-Epoetin Beta
parent: 僅模型預測 (L5)
nav_order: 573
evidence_level: L5
indication_count: 5
---

# Methoxy Polyethylene Glycol-Epoetin Beta
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

# Methoxy Polyethylene Glycol-Epoetin Beta：從腎性貧血相關用途到原發性血小板釋放障礙

## 一句話總結

Methoxy polyethylene glycol-epoetin beta（CERA，商品名 MIRCERA）是長效型紅血球生成刺激劑，在香港已有上市許可證。
TxGNN 模型預測它可能對**原發性血小板釋放障礙 (primary release disorder of platelets)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型運算結果。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料中未載明 |
| 預測新適應症 | 原發性血小板釋放障礙 (primary release disorder of platelets) |
| TxGNN 預測分數 | 99.36% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 CERA 是長效紅血球生成刺激劑 (ESA)，作用於紅血球生成素受體。

原發性血小板釋放障礙屬於血小板顆粒或訊號傳遞的內在缺陷，而紅血球生成素受體促效作用並無合理途徑矯正這類缺陷。因此，這個預測在機轉上**缺乏支持**，高分僅反映知識圖譜的網路關聯。

此外，ESA 具有血栓風險，對出血性疾病族群需特別謹慎。

**其他排名較前的預測（皆為 L5、Hold）：**

| 排名 | 預測適應症 | TxGNN 分數 | 評估 |
|------|-----------|-----------|------|
| 2 | Glanzmann 血小板無力症 | 99.30% | 病因為 integrin αIIbβ3 缺陷，ESA 無已知修復機轉；僅可能間接用於慢性失血貧血的支持治療 |
| 3 | 偽性血管性血友病 (pseudo-von Willebrand disease) | 99.25% | 病因為血小板 GP1BA 功能獲得性變異，與紅血球生成素訊號無明顯關聯 |
| 4 | 重度非增殖性糖尿病視網膜病變 | 99.15% | 五個候選中生物學上最合理（EPO 具神經保護與血管新生訊號），但 ESA 可能促進病理性血管新生、使視網膜病變惡化，安全方向不明 |
| 5 | 肝素輔因子 II 缺乏症 | 99.10% | ESA 無法調節 SERPIND1 路徑，且血栓風險在易栓體質下是安全疑慮 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-56445 | MIRCERA INJ 150MCG/0.3ML (PRE-FILLED SYRINGE) | 預填充注射劑 | 資料未載明 |
| HK-56442 | MIRCERA INJ 50MCG/0.3ML (PRE-FILLED SYRINGE) | 預填充注射劑 | 資料未載明 |
| HK-56450 | MIRCERA INJ 75MCG/0.3ML (PRE-FILLED SYRINGE) | 預填充注射劑 | 資料未載明 |
| HK-56449 | MIRCERA INJ 200MCG/0.3ML (PRE-FILLED SYRINGE) | 預填充注射劑 | 資料未載明 |
| HK-56447 | MIRCERA INJ 100MCG/0.3ML (PRE-FILLED SYRINGE) | 預填充注射劑 | 資料未載明 |

製造商均為 ROCHE HONG KONG LIMITED，5 張許可證皆為有效的單一成分製劑。

## 安全性考量

安全性資訊請參考原廠仿單。

另有一項來自機轉評估的提醒：ESA 類藥物具有血栓風險，在出血性或易栓性疾病、以及糖尿病視網膜病變情境下，需特別審慎評估。

## 結論與下一步

**決策：Hold**

**理由：**
- 五個預測適應症皆無臨床試驗或文獻佐證，證據等級僅為 L5，高 TxGNN 分數只是計算預測。
- 機轉上缺乏合理連結，且 ESA 的血栓風險與視網膜病變疑慮，使安全方向不明確。

**若要推進需要：**
- 取得香港仿單的核准適應症、警語與禁忌症資料
- 補充詳細的作用機轉（MOA）資料
- 若仍關注糖尿病視網膜病變方向，需先進行專門的前臨床與安全性審查
- 其餘血小板與凝血相關預測，建議不優先投入資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

