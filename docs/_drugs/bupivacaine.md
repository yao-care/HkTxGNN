---
layout: default
title: Bupivacaine
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 4
---

# Bupivacaine
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

# Bupivacaine：從皮膚炎到慢性萎縮性肢端皮膚炎

## 一句話總結

Bupivacaine 是一種醯胺類局部麻醉藥，在本次資料中的原適應症為皮膚炎 (dermatitis)。
TxGNN 模型預測它可能對**慢性萎縮性肢端皮膚炎 (Acrodermatitis chronica atrophicans)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 皮膚炎 (dermatitis)（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 慢性萎縮性肢端皮膚炎 (Acrodermatitis chronica atrophicans) |
| TxGNN 預測分數 | 99.23% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 9 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Bupivacaine 屬於醯胺類局部麻醉藥，一般認為是阻斷電壓門控鈉通道，但這並非來自本報告所整理的 MOA 欄位。

慢性萎縮性肢端皮膚炎是萊姆病（Borrelia 感染）的晚期皮膚表現，治療核心是抗生素。局部麻醉藥的鈉通道阻斷作用與清除感染無關，因此**現有資料無法支持任何機轉上的關聯**。

高分預測（99.23%）較可能反映知識圖譜中與「皮膚炎」類疾病節點的鄰近性，而非真實的療效訊號。

其他預測的新適應症也有相同情形，目前同樣沒有試驗或文獻支持：

| 排名 | 預測適應症 | TxGNN 分數 | 評估 |
|------|-----------|-----------|------|
| 2 | 新生兒皮肌炎 (Neonatal dermatomyositis) | 99.15% | 屬免疫介導疾病；bupivacaine 具肌肉毒性，是安全疑慮而非治療依據 |
| 3 | 兒童結締組織病相關次發性間質性肺病 | 99.11% | 無已知抗纖維化或免疫調節機轉；兒童使用需另行評估安全性 |
| 4 | 無肌病性皮肌炎 (Amyopathic dermatomyositis) | 99.03% | 最多只能推測局部緩解疼痛或搔癢，缺乏支持 |

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68545 | BUPIVACAINE HYPERBARIC SINTETICA SOLUTION FOR INJECTION 20MG/4ML | 注射液 | 未提供 |
| HK-64812 | BUPIVACAINE FOR SPINAL ANAESTHESIA AGUETTANT SOLUTION FOR INJECTION 5MG/ML | 注射液 | 未提供 |
| HK-63247 | REGIVELL SOLUTION FOR INJECTION 20MG/4ML | 注射液 | 未提供 |
| HK-42437 | MARCAIN SPINAL HEAVY INJ 0.5% | 注射液 | 未提供 |
| HK-35573 | MARCAIN POLYAMP DUOFIT 0.25% | 注射液 | 未提供 |

（本藥共有 9 張有效單方許可證，上表僅列 5 張。）

## 安全性考量

- **知識圖譜標示的禁忌疾病（非仿單內容）**：高血壓、低血壓、肝衰竭與肝病、腎臟病、癲癇、慢性阻塞性肺病、呼吸衰竭、心房顫動、冠狀動脈疾病、心肌梗塞、心臟傳導疾病、心臟驟停、糖尿病與糖尿病酮酸中毒、甲狀腺功能低下、發炎性腸道疾病、良性前列腺增生、血紅素病變、閉鎖角青光眼、物質濫用/依賴等。
- **藥物交互作用**：共查得 56 筆。中度等級的有 Aprepitant、Morphine (liposomal)；其餘如 Atropine、Vancomycin、Ondansetron、Metoclopramide、Dexamethasone、Prednisone、Simvastatin 等等級未明。
- 此外，bupivacaine 的肌肉毒性對預測的皮肌炎類適應症尤其值得注意。

其餘警語與禁忌的仿單內容請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 四項預測適應症皆只有模型分數，沒有臨床試驗或文獻，證據等級為 L5。
- 機轉上無法連結（慢性萎縮性肢端皮膚炎需抗生素治療），且部分適應症存在肌肉毒性疑慮。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌
- 補齊作用機轉（MOA）資料，重新分析機轉關聯
- 系統性檢索臨床試驗與文獻，確認是否有任何支持證據
- 釐清原適應症「皮膚炎」與局部麻醉藥實際用途之間的關係
- 若仍考慮推進，需先評估給藥途徑的可行性，並針對兒童族群進行安全性評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

