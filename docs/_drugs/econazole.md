---
layout: default
title: Econazole
parent: 僅模型預測 (L5)
nav_order: 306
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Econazole：預測新適應症為外陰陰道念珠菌症 (Vulvovaginal Candidiasis)，為證據最完整的候選（證據等級 L5）。原適應症：足癬、體癬、皮膚念珠菌症、花斑癬、鼠蹊與肛周皮癬菌病"
monitor_inn: "Econazole"
predicted_indications: ["Majocchi granuloma", "ectothrix infectious disease", "endothrix infectious disease"]
---

# Econazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Econazole：從皮膚黴菌感染到淺部黴菌症與外陰陰道念珠菌症

## 一句話總結

Econazole 是咪唑類（imidazole）抗黴菌藥，原本用於足癬、體癬、皮膚念珠菌症、花斑癬等皮膚黴菌感染。
TxGNN 模型預測它可能對多種黴菌相關疾病有效，其中證據最完整的是**外陰陰道念珠菌症 (Vulvovaginal Candidiasis)**，目前有 **0 個登記臨床試驗**，但有 **20 篇文獻**，其中包含多項與 clotrimazole 等藥物的對照臨床研究。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 足癬、體癬、皮膚念珠菌症、花斑癬、鼠蹊與肛周皮癬菌病（來自知識圖譜；香港許可證資料未載明適應症文字） |
| 預測新適應症 | 外陰陰道念珠菌症 (Vulvovaginal Candidiasis)，為證據最完整的候選；排名第 1 的預測為 Majocchi 肉芽腫 (Majocchi granuloma) |
| TxGNN 預測分數 | 外陰陰道念珠菌症 99.50%；Majocchi 肉芽腫 99.97% |
| 證據等級 | L3（外陰陰道念珠菌症）；其餘候選多為 L4–L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 16 張（皆為有效單方） |
| 建議決策 | Proceed with Guardrails（外陰陰道念珠菌症）；其他候選 Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Econazole 屬於咪唑類抗黴菌藥，一般認為是抑制黴菌 14-α-去甲基酶（lanosterol 14-alpha-demethylase），阻斷麥角固醇（ergosterol）合成，破壞黴菌細胞膜。這是類別層級的知識，並非來自本次資料中的 MOA 欄位。

原適應症（皮膚癬菌與皮膚念珠菌感染）與預測的新適應症高度相關：
- **外陰陰道念珠菌症**由 Candida 引起，而 Econazole 對皮膚念珠菌症本來就有效，機轉上可直接延伸。陰道用 Econazole 在多個國家已有使用，香港也有 150 mg 陰道栓劑的許可證，因此這比較像是已建立的用法，而非全新的再利用。
- **淺部黴菌症**與現有適應症大幅重疊，屬於標示內或接近標示內的使用。
- **Majocchi 肉芽腫、毛髮外/內感染、頭皮或鬍鬚癬菌病、深部癬 (tinea profunda)** 雖然機轉上說得通，但這些感染涉及毛囊或深層組織，外用藥穿透力有限，通常需要全身性抗黴菌治療。因此外用 Econazole 單獨使用不太可能足夠。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下以預測分數最高且證據最完整的**外陰陰道念珠菌症**為主，並補充其他候選的代表文獻。

### 外陰陰道念珠菌症

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7820892](https://pubmed.ncbi.nlm.nih.gov/7820892/) | 1994 | 雙盲對照臨床研究 | Ceylon Med J | Econazole 與 clotrimazole 治療陰道念珠菌症的療效比較 |
| [7383476](https://pubmed.ncbi.nlm.nih.gov/7383476/) | 1980 | 隨機對照 | Obstet Gynecol | 178 位女性，1% econazole 陰道乳膏與 clotrimazole 陰道錠黴菌學治癒率相近，局部不良反應低 |
| [2257961](https://pubmed.ncbi.nlm.nih.gov/2257961/) | 1990 | 隨機、單盲比較 | J Int Med Res | 比較 butoconazole 乳膏（3 天）與 econazole 乳膏（7 天）治療外陰陰道念珠菌症 |
| [7428415](https://pubmed.ncbi.nlm.nih.gov/7428415/) | 1980 | 多中心隨機比較 | Curr Med Res Opin | 三天療程，econazole 150 mg 陰道栓與 clotrimazole 200 mg 陰道錠的比較 |
| [6761088](https://pubmed.ncbi.nlm.nih.gov/6761088/) | 1982 | 多中心隨機比較 | Chemotherapy | 同上研究的另一份報告 |
| [984105](https://pubmed.ncbi.nlm.nih.gov/984105/) | 1976 | 多中心臨床研究 | Am J Obstet Gynecol | 996 位患者，150 mg 陰道栓三日療法，前兩項研究（880 人）總治癒率 93.4% |
| [98315](https://pubmed.ncbi.nlm.nih.gov/98315/) | 1978 | 綜述 | Drugs | Econazole 的抗黴菌活性與治療效果回顧 |
| [25442913](https://pubmed.ncbi.nlm.nih.gov/25442913/) | 2014 | 體外研究 | J Mycol Med | 200 株 Candida 臨床分離株對咪唑類與 nystatin 的敏感性 |
| [37601561](https://pubmed.ncbi.nlm.nih.gov/37601561/) | 2023 | 體外／抗藥性研究 | Infect Drug Resist | 生物膜形成與天冬胺酸蛋白酶活性和 C. albicans 唑類抗藥性相關 |

### 其他候選適應症

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7351270](https://pubmed.ncbi.nlm.nih.gov/7351270/) | 1980 | 追蹤研究 | Dermatologica | 100 位淺部黴菌症患者以 econazole 1% 治療，追蹤 83 位，95% 無復發或再感染 |
| [153658](https://pubmed.ncbi.nlm.nih.gov/153658/) | 1978 | 臨床研究（非隨機） | Z Hautkr | Econazole 噴液與噴粉用於皮膚黴菌症（頭皮或鬍鬚癬菌病候選中唯一以 econazole 為主的臨床紀錄，與頭皮疾病的關聯不明） |
| [42256225](https://pubmed.ncbi.nlm.nih.gov/42256225/) | 2026 | 臨床／微生物研究 | Front Cell Infect Microbiol | 外耳道黴菌症中 econazole 最低抑菌濃度與臨床反應的相關性 |
| [37899944](https://pubmed.ncbi.nlm.nih.gov/37899944/) | 2023 | 病例報告 | Case Rep Dermatol | Majocchi 肉芽腫病例，未顯示 econazole 的療效 |
| [15919146](https://pubmed.ncbi.nlm.nih.gov/15919146/) | 2005 | 前臨床 | Food Chem Toxicol | Econazole 對大腸癌細胞 COLO 205 的細胞毒性（與本報告適應症無直接關係） |

**說明：**淺部黴菌症的其他文獻多為其他唑類藥物（bifonazole、sulconazole、tioconazole、sertaconazole、fenticonazole、itraconazole）的回顧，僅能間接支持類別效應。多數較早期的研究設計與品質無法僅從標題確認。

---

## 香港上市資訊

香港共有 16 張有效的單方許可證，以下列出 5 張。許可證資料中未載明劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-36295 | ECOMI VAGINAL PESSARIES 150MG | 陰道栓劑（依品名） | 資料未載明 |
| HK-34621 | ECONAZOLE SUPP 150MG "YUNG SHIN" | 栓劑（依品名） | 資料未載明 |
| HK-57772 | ZYME SOLUTION 10MG/ML | 溶液（依品名） | 資料未載明 |
| HK-58828 | EKONA VAGINAL SUPP 150MG | 陰道栓劑（依品名） | 資料未載明 |
| HK-54354 | PICOSONE CREAM | 乳膏（依品名） | 資料未載明 |

其餘 11 張多為乳膏產品（如 ECONAZINE、EPARCORT、ECOLEX 等），其中部分品名暗示為含皮質類固醇的複方，但許可證資料標示為單方，故未下結論。

---

## 安全性考量

- **藥物交互作用**：資料庫共查得 41 筆交互作用，但嚴重度等級皆為「未知」。已列出的藥物包括 clotrimazole、fluconazole、metformin、omeprazole、rosiglitazone、glipizide、dexamethasone、clopidogrel、heparin 等。尚無法依嚴重度排序，臨床使用前應逐項查核。

其餘警語與禁忌症資料，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails（外陰陰道念珠菌症）；其餘候選 Hold**

**理由：**
- 外陰陰道念珠菌症有多項 econazole 對照臨床研究（含與 clotrimazole 的隨機比較），且香港已有陰道栓劑許可證，屬證據等級 L3，實質上接近既有用法。
- Majocchi 肉芽腫、毛髮外／內感染、頭皮或鬍鬚癬菌病、深部癬僅有模型預測或零星病例報告，且外用藥穿透力不足，應暫緩（Hold）。
- 淺部黴菌症與現有適應症大幅重疊，主要屬標示內使用，較適合視為研究問題而非再利用。

**若要推進需要：**
- 取得香港許可證的核准適應症與仿單警語、禁忌症（目前為阻擋性資料缺口）
- 補充詳細作用機轉資料（DrugBank）
- 確認各陰道用許可證實際核准的適應症，判斷外陰陰道念珠菌症是否已在標示內
- 評估當地 Candida 菌株對唑類的抗藥性與生物膜因素
- 取得 41 筆藥物交互作用的嚴重度分級
- 對毛囊或深部感染，需評估是否須合併全身性治療，再決定是否進一步研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

