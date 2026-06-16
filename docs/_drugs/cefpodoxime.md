---
layout: default
title: Cefpodoxime
parent: 僅模型預測 (L5)
nav_order: 148
evidence_level: L5
indication_count: 10
---

# Cefpodoxime
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

# Cefpodoxime：從細菌感染到骨關節炎易感性

## 一句話總結

Cefpodoxime 是第三代口服頭孢菌素類抗生素，原本用於治療細菌感染（如呼吸道感染、泌尿道感染）。
TxGNN 模型預測它可能與**骨關節炎易感性 (Osteoarthritis Susceptibility)** 相關，
然而目前**無任何臨床試驗或文獻**支持此方向，所有預測均停留在模型推測階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 細菌感染（口服頭孢菌素類抗生素） |
| 預測新適應症 | 骨關節炎易感性 (Osteoarthritis Susceptibility) |
| TxGNN 預測分數 | 99.35% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Cefpodoxime 屬於 β-lactam 頭孢菌素類（Cephalosporin）抗生素，藉由抑制細菌細胞壁合成（PBP 結合）發揮殺菌效果，是廣泛使用的口服第三代頭孢菌素。

TxGNN 知識圖譜的預測邏輯可能源自兩個間接路徑：其一是部分 β-lactam 抗生素（尤其是 ceftriaxone）在動物模型中展現 GLT-1 谷氨酸轉運體上調效果；其二是四環素類抗生素（minocycline、doxycycline）具有 MMP 抑制與抗炎活性，在 OA 動物模型中有保護作用，KG 可能將此類「抗生素→炎症節點→骨關節炎」的間接路徑連結至 Cefpodoxime。

然而，頭孢菌素類對 MMP 的抑制活性遠弱於四環素類，且針對 Cefpodoxime 本身完全無骨關節作用的直接機轉數據。值得注意的是，排名前十的預測幾乎全為骨骼發育相關罕見遺傳病（brachyolmia、pseudoachondroplasia 等），此聚集現象強烈提示 KG 中骨/軟骨節點的結構性雜訊，而非真實藥物-疾病關聯。

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
所有 10 個預測適應症均為 L5 等級（純模型預測，無任何臨床試驗或文獻支持），且機轉連結屬高度推測性；預測結果聚集於骨骼發育疾病節點，反映知識圖譜結構性雜訊而非真實藥理信號。此外，Cefpodoxime 在香港尚未上市（0 張許可證），再利用的監管基礎亦待建立。

**若要推進需要：**
- 確認 Cefpodoxime 詳細 MOA 資料（DrugBank API 查詢）
- 補充 TFDA/香港 Department of Health 仿單安全性警語與禁忌資料
- 以 Cefpodoxime 類別抗生素對 MMP/NF-κB 的體外或動物研究做初步機轉驗證，再評估是否值得投入更高等級證據收集
- 若考慮香港市場，需先完成藥品上市申請
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

