---
layout: default
title: Doxycycline
parent: 中證據等級 (L3-L4)
nav_order: 219
evidence_level: L4
indication_count: 10
---

# Doxycycline
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

# Doxycycline：從廣效抗菌感染到點狀上皮角結膜炎

## 一句話總結

Doxycycline 是一種四環素類廣效抗生素，廣泛用於治療衣原體、立克次體、萊姆病、非典型肺炎等多種細菌感染。TxGNN 模型預測它可能對**點狀上皮角結膜炎 (Punctate Epithelial Keratoconjunctivitis)** 有效，目前有 **0 個臨床試驗**和 **1 篇文獻**支持這個方向，整體證據極為初步。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 廣效細菌感染（衣原體、立克次體、萊姆病、非典型肺炎等） |
| 預測新適應症 | 點狀上皮角結膜炎 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Research Question |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Doxycycline 屬四環素類廣效抗生素，透過與細菌 **30S 核醣體亞基**可逆性結合，阻斷胺醯基-tRNA 進入核醣體接受位，從而抑制蛋白質合成。此機轉對胞內寄生菌（Chlamydia、Rickettsia、Mycoplasma、Borrelia 等）尤其有效，使其成為多種非典型感染的一線用藥。

點狀上皮角結膜炎（PEK）可由多種病因引起，其中**沙眼衣原體（Chlamydia trachomatis）**引起的沙眼性角結膜炎是重要病因之一。TxGNN 知識圖譜可能透過「Doxycycline → Chlamydia 清除 → 角結膜炎改善」的間接路徑推導出此預測，具備一定的生物學邏輯。

然而，現有唯一文獻描述的是沙眼性結膜炎以 Doxycycline **治療後**濾泡消退，卻仍持續出現雙側點狀角膜上皮病變的案例——顯示該病變為**感染後續發症（post-infectious sequelae）**，而非 Doxycycline 的直接治療靶點。機轉連結屬間接性，臨床意義需進一步研究釐清。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case Series | *Cornea* | 2 例沙眼衣原體濾泡性結膜炎，以口服四環素或 Doxycycline 治療後濾泡消退，但隨後出現復發性、雙側灰白色點狀角膜上皮病變，其中一例伴有前基質水腫。顯示此角膜病變為感染後持續症，而非 Doxycycline 直接治療目標 |

---

## 香港上市資訊

Doxycycline 在香港目前**未上市**，無相關藥品許可證記錄。如需臨床使用，需透過特別進口申請或參考其他地區（如台灣、日本）已核准仿單資訊。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Research Question**

**理由：**
現有機轉連結屬間接性——唯一相關文獻為 1992 年的 2 例病案報告，描述的是感染後持續性角膜病變，而非 Doxycycline 直接治療點狀上皮角結膜炎的效果。香港無上市記錄，安全性資料與 MOA 資訊均缺乏，尚不具備進入正式再利用評估的條件。

**若要推進需要：**
- 針對「衣原體相關點狀角膜炎」進行系統性文獻回顧，釐清 Doxycycline 的直接與間接治療潛力
- 補充 Doxycycline 作用機轉（MOA）詳細資料（建議查詢 DrugBank API）
- 查閱原廠仿單取得完整警語、禁忌及藥物交互作用資訊
- 評估眼科局部給藥的可行性與安全性
- 考量轉而聚焦其他證據等級較高的預測適應症（如「感染後細菌疾病」L1 / 「感染後症候群」L2 / 「慢性牙齦炎」L2）

---

> ⚠️ **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。所有老藥新用候選需經過臨床驗證才能應用於實際臨床情境。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

