---
layout: default
title: Ceftaroline Fosamil
parent: 僅模型預測 (L5)
nav_order: 149
evidence_level: L5
indication_count: 10
---

# Ceftaroline Fosamil
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

The txgnn-pipeline skill is a general orchestration guide — the detailed report format is already fully specified in the system prompt. Proceeding to generate the report.

---

# Ceftaroline fosamil：從細菌感染治療到類風濕性關節炎

## 一句話總結

Ceftaroline fosamil 是第五代頭孢菌素類抗生素前藥，具備對抗 MRSA（耐甲氧西林金黃色葡萄球菌）的活性，臨床上用於社區獲得性肺炎（CABP）與急性皮膚及皮膚結構感染（ABSSSI）的治療。
TxGNN 模型預測它可能對**類風濕性關節炎 (Rheumatoid Arthritis)** 有效，預測分數高達 **98.20%**，但目前**完全無臨床試驗**、**無支持性文獻**，且藥理機轉上與 RA 缺乏任何生物學關聯，研判此為模型假陽性。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 社區獲得性細菌性肺炎（CABP）、急性皮膚及皮膚結構感染（ABSSSI，含 MRSA） |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 98.20% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA Data Gap）。根據已知藥理知識，Ceftaroline fosamil 是一種前藥，在體內轉化為活性型 Ceftaroline 後，透過共價結合細菌的青黴素結合蛋白（Penicillin-Binding Proteins, PBPs）——尤其是 PBP2a——抑制細菌細胞壁合成，進而達到殺菌效果。PBP2a 正是 MRSA 對傳統 β-內醯胺類抗生素產生抗藥性的關鍵蛋白，因此 Ceftaroline 在第五代頭孢菌素中具有特殊的抗 MRSA 地位。

類風濕性關節炎（RA）是一種系統性自體免疫疾病，其核心病理機制為 T 細胞與 B 細胞功能失調，以及 TNF-α、IL-6、IL-17 等促炎細胞激素的過度表達，最終導致滑膜增生與骨侵蝕。這與抗生素作用靶點（細菌 PBP）在生物學上**毫無交集**。

因此，雖然 TxGNN 給出 0.982 的高分，但此高分最可能的原因是知識圖譜中「關節炎相關節點」的圖譜擴散效應（graph diffusion artifact）。綜觀所有 10 項預測（涵蓋 RA、OA、痛風、骨骼發育異常、肌硬化症等），無一具備合理的機轉關聯，呈現出典型的抗生素-關節/骨骼疾病假陽性模式，**此藥物在這批預測適應症中不具再利用潛力**。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻（針對類風濕性關節炎適應症）。

> **附註：** 在所有 10 項預測適應症中，僅找到 3 篇文獻，且均與預測適應症無直接關聯：
> - 2 篇關於「骨關節腔細菌感染（osteoarticular infection）」的抗生素選擇，實為 Ceftaroline 的既有感染適應症，非再利用；
> - 1 篇為 2011 年新藥評論，同期介紹 Ceftaroline（抗感染）、Pegloticase（抗痛風）、Eribulin（抗癌）三種完全不同藥物，文獻共現不代表療效關聯。

---

## 香港上市資訊

Ceftaroline fosamil 目前在香港**未上市**，無任何已登記許可證。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
Ceftaroline fosamil 是作用於細菌 PBP 的抗生素，而 TxGNN 預測的全部 10 項適應症均為非感染性疾病（自體免疫、退化性、遺傳發育異常）。兩者在藥理機轉上無任何生物學交集，所有預測均具典型圖譜擴散假陽性特徵（零臨床試驗、文獻均為無關共現、無機轉路徑支持），不建議投入再利用研究資源。

**若要推進需要：**
- 重新聚焦於 Ceftaroline 的**本業感染適應症延伸**（例如骨髓炎、人工關節感染、醫院獲得性肺炎、菌血症），而非非感染性疾病再利用
- 補充完整作用機轉資料（DrugBank MOA API 查詢）
- 評估在香港申請上市許可的可行性（目前 0 張許可證），以解鎖感染症既有適應症的市場准入
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

