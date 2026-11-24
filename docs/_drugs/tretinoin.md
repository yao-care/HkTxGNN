---
layout: default
title: Tretinoin
parent: 僅模型預測 (L5)
nav_order: 902
evidence_level: L5
indication_count: 9
monitor_inn: "TRETINOIN"
predicted_indications: ["rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "juvenile idiopathic arthritis", "juvenile chronic polyarthritis", "juvenile arthritis due to defect in LACC1", "osteoarthritis", "pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type", "Quinquaud's folliculitis decalvans"]
last_modified_at: 2026-11-24
description: "Tretinoin：預測新適應症為類風濕性結節病 (Rheumatoid Nodulosis)（證據等級 L5）。原適應症：知識圖譜中記錄的關聯為痤瘡、急性前骨髓性白血病、後天性角化症、掌蹠角化症"
---

# Tretinoin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Tretinoin：從痤瘡與急性前骨髓性白血病到類風濕性結節病
{: .text-alpha }

## 一句話總結

Tretinoin（全反式維生素 A 酸）在知識圖譜中記錄的用途包括痤瘡、急性前骨髓性白血病、後天性角化症與掌蹠角化症。
TxGNN 模型預測它可能對**類風濕性結節病 (Rheumatoid Nodulosis)** 有效，但目前**沒有任何臨床試驗或直接相關文獻**支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜中記錄的關聯為痤瘡、急性前骨髓性白血病、後天性角化症、掌蹠角化症（許可證資料未載明核准適應症文字） |
| 預測新適應症 | 類風濕性結節病 (Rheumatoid Nodulosis) |
| TxGNN 預測分數 | 0.9984 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 12 張／共 12 張） |
| 許可證數 | 12 張（有效 12 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Tretinoin 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Tretinoin 於培養及體內環境中可誘導 APL 細胞之細胞分化並減少其增生。在 APL 病人中，tretinoin 治療會先使源自白血病細胞株之原始前骨髓細胞成熟，隨後在達到完全緩解（CR）之病人中，骨髓及周邊血液由正常、多株性造血細胞重新填補。」英文原文："Tretinoin induces cytodifferentiation and decreased proliferation of APL cells in culture and in vivo. In APL patients, tretinoin treatment produces an initial maturation of the primitive promyelocytes derived from the leukemic clone, followed by a repopulation of the bone marrow and peripheral blood by normal, polyclonal hematopoietic cells in patients achieving complete remission (CR)."（[DailyMed: tretinoin prescribing information, Par Health USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9c4ae9d9-c2a0-4995-a27a-e3f0f0284db9)，版本日期 2026-08-20；查閱日期 2026-11-19）。根據已知資訊，tretinoin 是維生素 A 酸類（retinoid）藥物，透過視黃酸受體調控細胞分化與增生。

視黃酸具有免疫調節作用，例如可能影響 Th17/Treg 平衡與發炎細胞激素，理論上可能與類風濕譜系的發炎有關。但目前沒有任何資料顯示它與類風濕性結節的形成有直接關聯。這個高分預測來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而非生物學證據，應視為假說，而非有實證支持的結論。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對此預測適應症，目前未檢索到直接研究類風濕性結節病的文獻。

---

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-40621 | VESANOID CAP 10MG | 單一成分 | DKSH HONG KONG LIMITED | 有效 |
| HK-57254 | ACNETIN-A CREAM 0.05% | 單一成分 | GAILY PHARMACEUTICAL COMPANY LIMITED | 有效 |
| HK-32929 | ACTA CREAM 0.1% | 單一成分 | JEAN-MARIE PHARMACAL CO LTD | 有效 |
| HK-65326 | VITACID CREAM 0.05%W/W | 單一成分 | HEALTHCARE PHARMASCIENCE LIMITED | 有效 |
| HK-58939 | KETREL CREAM 0.05% | 單一成分 | LABORATOIRES BAILLEUL LIMITED | 有效 |

上表列出其中 5 張（共 12 張）。

<!-- licenses:end -->

以上列出部分主要許可證；含本藥成分的許可證包括單一成分與複方製劑，張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表。

<!-- review:begin hk-lic-20261124b-tretinoin-1 -->

> **查核更正（2026-11-24）**：原文為「以上列出 5 張主要許可證，共 12 張，皆為單方、有效狀態。」。已更正：依衞生署藥物辦公室註冊名單的成分欄，含本藥成分的許可證包括單一成分與複方製劑；原句的單一成分／複方說法或張數跟註冊名單不符（舊報告依證據包以「;;」切成分，每張都算成單方）。張數見本頁快速總覽與許可證表（2026-11-24 核對）。依據：[衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261124b-tretinoin-1 -->

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 非傳統細胞毒性藥物（分化誘導劑，用於急性前骨髓性白血病） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **知識圖譜中記錄的禁忌關聯**（非仿單內容）：曬傷、焦慮症、精神病類疾病、腎臟疾病、肝臟疾病、胰臟炎、膽囊疾病、充血性心衰竭、腎上腺皮質功能不全、克隆氏症與發炎性腸道疾病、異位性皮膚炎、骨質疏鬆、蕈樣肉芽腫與皮膚 T 細胞淋巴瘤、糖尿病與糖尿病酮酸中毒等。
- **藥物交互作用**（共 100 筆，列出主要者）：
  - 重大 (Major)：Doxycycline、Tetracycline、Minocycline、Vitamin A
  - 中度 (Moderate)：Aprepitant、Clarithromycin、Naltrexone
  - 輕微 (Minor)：Levofloxacin
- **與預測適應症相關的風險**：全身性視黃酸類藥物具致畸胎性與骨骼毒性，若用於兒童關節炎族群需特別謹慎。

詳細警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 類風濕性結節病的預測僅來自模型，沒有臨床試驗或直接文獻支持，證據等級為 L5。
- 機轉連結尚屬假說，且全身性視黃酸類藥物有明確的安全性疑慮。

**若要推進需要：**
- 取得作用機轉資料，並檢視視黃酸對類風濕性結節形成的前臨床證據
- 進行文獻與病例系列回顧，確認是否有任何直接證據
- 取得香港仿單的警語、禁忌與核准適應症資料，完成安全性篩選

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: tretinoin prescribing information, Par Health USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9c4ae9d9-c2a0-4995-a27a-e3f0f0284db9) |
| 2026-11-24 | 「以上列出 5 張主要許可證，共 12 張，皆為單方、有效狀態。」→「以上列出部分主要許可證；含本藥成分的許可證包括單一成分與複方」 | 更正 | [衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

