---
layout: default
title: Imiglucerase
parent: 中證據等級 (L3-L4)
nav_order: 392
evidence_level: L4
indication_count: 10
---

# Imiglucerase
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

直接依照使用者提供的 v5 Prompt 規格產生報告，此為純資料萃取與文字撰寫任務，不涉及程式碼修改、除錯或需要腦力激盪的功能設計，故不套用額外技能，直接依規則輸出。

以下是根據 Evidence Pack 產生的報告：

---

# Imiglucerase：從高雪氏症（Gaucher Disease）到 Hurler 症候群（黏多醣症第一型）

## 一句話總結

> Imiglucerase 是基因重組人類 glucocerebrosidase（葡萄糖腦苷脂酶）替代療法藥物，原用於治療高雪氏症（Gaucher disease）。
> TxGNN 模型預測它可能對 **Hurler 症候群 (Hurler Syndrome，黏多醣症第一型)** 有效，
> 但目前**無臨床試驗**支持，僅有 **2 篇文獻**（皆為一般性酵素替代療法回顧），且機轉分析顯示此預測可能只是知識圖譜中「溶酶體儲積症」類別的結構性群聚效應，而非真實的酵素受質重疊。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高雪氏症 (Gaucher disease)（文獻佐證；無香港許可證資料可查證） |
| 預測新適應症 | Hurler 症候群 (Hurler Syndrome，黏多醣症第一型) |
| TxGNN 預測分數 | 99.52% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測合理？

目前缺乏 Imiglucerase 詳細的作用機轉資料（DrugBank MOA 為資料缺口）。根據文獻證據，Imiglucerase 是基因重組的 glucocerebrosidase（葡萄糖腦苷脂酶），用於補充高雪氏症患者體內缺乏的此酵素，屬於鞘脂類（glycosphingolipid）代謝路徑的酵素替代療法 (ERT)。

然而，Hurler 症候群屬於黏多醣症第一型 (MPS I)，致病原因是 **alpha-L-iduronidase (IDUA)** 酵素缺乏，導致的是黏多醣（glycosaminoglycan）代謝異常，與 glucocerebrosidase 所處理的鞘脂類代謝屬於**完全不同的生化路徑**。兩者唯一的共同點是同屬「溶酶體儲積症 (lysosomal storage disease)」這個大分類。

根據 Evidence Pack 內附的機轉分析，此高分預測**很可能源自 TxGNN 知識圖譜中「溶酶體儲積症」節點群的結構相似性，而非藥物與疾病間真實的酵素受質重疊**。換言之，這是模型對疾病大類的泛化預測，機轉關聯薄弱甚至可能是錯誤的，需謹慎解讀。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [20534487](https://pubmed.ncbi.nlm.nih.gov/20534487/) | 2010 | Review | PNAS | 以 PET 造影評估多種溶酶體儲積症（含高雪氏症、Hurler 症候群等）的酵素替代療法分佈情形，屬跨疾病通論性文章，非 Hurler 症候群專屬研究 |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | La Revue de medecine interne | 回顧溶酶體儲積症酵素替代療法發展史（含 alglucerase/imiglucerase 用於高雪氏症、Fabry disease 等），未針對 Hurler 症候群提出具體療效證據 |

**註**：以上兩篇文獻皆非針對 Imiglucerase 治療 Hurler 症候群的直接研究，僅為酵素替代療法的通論性回顧。

---

## 香港上市資訊

目前無香港上市許可證登記（market_status：未上市，total_licenses：0）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 唯一支持證據為 2 篇非疾病特異性的通論回顧文獻，且無任何臨床試驗登記，證據等級僅 L4。
- 機轉分析顯示 Hurler 症候群（IDUA 酵素缺乏，黏多醣代謝）與 Imiglucerase 標的（glucocerebrosidase，鞘脂類代謝）分屬不同代謝路徑，此預測極可能為 TxGNN 對「溶酶體儲積症」類別群聚所致的假陽性，不建議投入研究資源推進。
- 補充：本 Evidence Pack 中其他 9 個預測適應症（rank 2-10）亦均判定為 Hold，多數為 L5（僅模型預測、零試驗零文獻），唯一例外是 rank 6「lysosomal storage disease with skeletal involvement」有較多臨床試驗與文獻支持，但該項實質上是高雪氏症骨骼併發症的既有治療管理，而非真正的「新」適應症。

**若要推進需要：**
- 補充香港/台灣仿單警語與禁忌症資料（目前為 Blocking 等級資料缺口，無法進入 S1 安全性初評）
- 補充 Imiglucerase 完整作用機轉 (MOA) 資料（查詢 DrugBank API），釐清是否存在任何與黏多醣代謝路徑相關的旁證
- 若仍考慮推進，應先進行體外或動物模型驗證，確認 glucocerebrosidase 補充是否對 IDUA 相關代謝路徑有任何實質影響（目前無此類機轉證據）
- 確認香港上市與藥證申請可行性（目前完全未上市，無許可證資料）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

